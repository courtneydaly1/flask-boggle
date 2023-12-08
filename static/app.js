class BoggleGame {
    constructor(boardId, secs= 60) {
        this.secs =secs;
        this.shoeTimer();
        this.score =0;
        this.words= new Set();
        this.board = $("#" + boardId);
        //tick every 100 msec
        this.timer =setInterval(this.tick.bind(this), 1000);
        $(".addword", this.board).on("submit", this.handleSubmit.bind(this));
    }

//show word in the list of words
showWord(word)  {
    $(".word", this.board).append($("<li>", { text: word}));
}

//show score in html
showScore(){
    $(".score", this.board).text(this.score);
}

//show status message
showMessage(msg,cls) {
    $(".msg", this.board).text(msg).removeClass().addClass('msg ${cls}');
}

//handle submission of word, if valid show and upate score
async handleSubmit(event) {
    event.preventDefault();
    const $word = $(".word", this.board);
    let word =$word.val();
    if (!word) return;

    if (this.word.has(word)){
        this.showMessage(`Already found ${word}`, "err");
        return;
    }

    //check server for valid word
    const res = await axios.get("/check-word", {params: {word: word}});
    if (res.data.result === "not-word"){
        this.showMessage(`${word} is not a valid word`, "err");
    }
    else if (res.data.result === "not-on-board"){
        this.showMessage(`${word} is not a valid word on this board`, "err");
    }
    else{
        this.showWord(word);
        this.score+= word.length;
        this.showScore();
        this.word.add(word);
        this.showMessage(`Added: ${word}`, "ok");
    }

    $word.val("").focus();
}

//update timer
showTimer() {
    $(".timer", this.board).text(this.secs);
}

//ticks handler
async tick() {
    this.secs -= 1;
    this.showTimer();

    if(this.secs=== 0){
        clearInterval(this.timer);
        await this.scoreGame();
    } 
}

//end of game score and message
async scoreGame() {
    $(".add-word", this.board).hide();
    const res = await axios.post('/post-score', { score:this.score });
    if (res.data.brokeRecord) {
        this.showMessage(`NEW RECORD: ${this.score}!`, "ok");
    }
    else {
        this.showMessage(`Final Score: ${this.score}`, "ok");
    }
}
}
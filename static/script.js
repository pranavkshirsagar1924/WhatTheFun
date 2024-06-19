function make_comment() {
    let a = document.getElementById('t');
    fetch('/comment?data=' + encodeURIComponent(a.value))
        .then(response => {
            if (response.ok) {
                console.log(response);
                return response.text();
            } else {
                console.error('Request failed with status: ' + response.status);
            }
        }).then(data => {
            add_comment(a.value,JSON.parse(data).stat);
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}
function add_comment(comment,state_){
    const div = document.createElement('div');
        div.innerHTML = `<b>You</b><p>${comment}</p>`;
    if(state_ == 'NSFW'){
        div.className = 'red_comment';
    }else{
        div.className = 'green_comment';
    }
    const cb = document.getElementById('comment-board');
        cb.appendChild(div);
}

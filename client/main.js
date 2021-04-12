function main() {
    console.log('test')
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8000/users', false);
    let aggIdEl = document.getElementById('agg_id')
    let familyNameEl = document.getElementById('family_name')
    try{
        xhr.send();
        const data = JSON.parse(xhr.response).data
        aggIdEl.innerHTML = data.agg_id
        familyNameEl.innerHTML = data.family_name
    } catch {
        document.getElementById('errorBlock').innerHTML = "Server disconnected"
    }

}
main()
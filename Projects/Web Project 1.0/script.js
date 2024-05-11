const quote = document.getElementById("quote");
const author = document.getElementById("author");
const api_url = 'https://api.quotable.io/random';

async function get_quote(url){
    const response = await fetch(url);
    var data = await response.json()
    quote.innerHTML = data.content;
    author.innerHTML = data.author;
}

get_quote(api_url);
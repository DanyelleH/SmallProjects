document.querySelector('button').addEventListener('click', getFetch);
async function getFetch() {
    const isChecked = document.querySelector("#shinyCheck").checked
    const choice = document.querySelector('input').value.toLowerCase()
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice
    
    let data = await fetch(url);
    let pokemonInfo = await data.json();
    let pokemonName = pokemonInfo.name;
    document.querySelector("#name").innerText = pokemonName;

    let pokemonType = pokemonInfo.types[0].type.name;
    document.querySelector("#type").innerText= pokemonType;

    
    let pokemonImage = pokemonInfo.sprites.front_default;
    if (pokemonImage) {
        document.querySelector("#mainImg").src= pokemonInfo.sprites.front_default;
    } else{
        document.querySelector("#pokemonImage").alt= "No Image Available";
    }

    if (isChecked) {
        document.querySelector("#mainImg").src = pokemonInfo.sprites.front_shiny
    }
    console.log(pokemonInfo)
} 
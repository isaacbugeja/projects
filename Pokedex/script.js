const outputContainer = document.getElementById("result-output");
const userInput = document.getElementById("user-input");
const searchBtn = document.getElementById("search-btn");
const pokemonName = document.getElementById("pokemon-name");
const pokemonNumber = document.getElementById("pokemon-number");
const pokemonType = document.getElementById("pokemon-type");
const pokemonStats = document.getElementById("pokemon-stats");
const pokemonSprite = document.getElementById("pokemon-sprite");
const fetchPokemon = async () => {
    try{
        const pokemonNameOrId = userInput.value.toLowerCase();
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonNameOrId}`);
        if(!response.ok){
            throw new Error('Pokémon was not found');
        };
        const data = await response.json();
        pokemonName.textContent = data.name.charAt(0).toUpperCase() + data.name.slice(1);
        pokemonNumber.textContent = `#${data.id}`;
        pokemonSprite.innerHTML =  `<img src = "${data.sprites.front_default}" alt="Pokemon Sprite" class="sprite">
                                    <img src = "${data.sprites.front_shiny}" alt = "Pokemon Shiny Sprite" class="sprite">`;
        
        //Set Pokemon Types
        pokemonType.innerHTML= data.types
            .map(obj => `<span class="type ${obj.type.name}">${obj.type.name}</span>`)
            .join('');
        
        //Set Pokemon Stats
        pokemonStats.innerHTML =`
                                <table>
                                    <thead>
                                        <tr>
                                            <th>Weight (in kg)</th>
                                            <th>Height (in metres)</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td style="font-weight: normal;">${(data.weight)/10}kg</td>
                                            <td style="font-weight: normal;">${(data.height)/10}m</td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table>
                                    <thead>
                                        <tr>
                                            <th>Base</th>
                                            <th>Stats</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>HP</td>
                                            <td >${data.stats[0].base_stat}</td>
                                        </tr>
                                        <tr>
                                            <td>Attack</td>
                                            <td>${data.stats[1].base_stat}</td>
                                        </tr>
                                        <tr>
                                            <td>Defense</td>
                                            <td>${data.stats[2].base_stat}</td>
                                        </tr>
                                        <tr>
                                            <td>Special Attack</td>
                                            <td>${data.stats[3].base_stat}</td>
                                        </tr>
                                        <tr>
                                            <td>Special Defense</td>
                                            <td>${data.stats[4].base_stat}</td>
                                        </tr>
                                        <tr>
                                            <td>Speed</td>
                                            <td>${data.stats[5].base_stat}</td>
                                        </tr>
                                    </tbody>
                                </table>`
        
    }catch (err){
        alert(err.message);
    };
};

function searchPokemon() {
    if (userInput.value === "") {
        alert("Please enter a Pokémon to search.");
        return;
    }
    fetchPokemon();
    userInput.value = "";
}

searchBtn.addEventListener("click", ()=>{
    searchPokemon();

});

userInput.addEventListener("keydown", (e) =>{
    if(e.key==="Enter"){
        searchPokemon();
    }
});





/** TO ADD THE FOLLOWING:
 * 
 *  https://pokeapi.co/api/v2/characteristic/{id}/ - pass ID of pokemon
 *  
 * 
 * get descriptions.description && descriptions.language = "en"
 * 
 * 
 */
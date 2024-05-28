
const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "brown", moons: 79 },
    { name: "Saturn", color: "yellow", moons: 82 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "blue", moons: 14 }
];


function createSolarSystem() {
    const section = document.querySelector('.listPlanets');

    
    planets.forEach(planet => {
        const planetDiv = document.createElement('div');
        planetDiv.classList.add('planet', planet.name.toLowerCase());
        planetDiv.style.backgroundColor = planet.color;
        planetDiv.textContent = planet.name;

        
        section.appendChild(planetDiv);

        
        if (planet.moons > 0) {
            for (let i = 0; i < planet.moons; i++) {
                const moonDiv = document.createElement('div');
                moonDiv.classList.add('moon');
                moonDiv.style.backgroundColor = "rgb(237, 237, 237)";
                moonDiv.style.left = `${Math.random() * 80 + 10}%`;
                moonDiv.style.top = `${Math.random() * 80 + 10}%`;

                
                planetDiv.appendChild(moonDiv);
            }
        }
    });
}


createSolarSystem();

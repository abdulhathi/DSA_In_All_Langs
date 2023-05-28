"use strict";

const getCountryData = (countryName) => {
  const request = new XMLHttpRequest();
  request.open("GET", "https://restcountries.com/v3.1/name/"+ countryName);
  request.send();


  request.addEventListener('load', function() {
    const [data] = JSON.parse(this.responseText);
    console.log(data.flags["png"]);
    console.log(data);
    const conuntriesContainer = document.querySelector(".countriesContainer");

    const html = `<div class="countryCard">
      <h1>${data.name["common"]}</h1>
      <img src="${data.flags["png"]}"></img>
    </div>`;
    // console.log(conuntriesContainer);
    conuntriesContainer.insertAdjacentHTML("beforeend", html);
  });
}

getCountryData("india")
getCountryData("usa")
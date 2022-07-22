// Create a function that renders the three team images
// Use a for loop, template strings (``), plus equals (+=)
// .innerHTML to solve the challenge.

const imgs = [
    "images/hip1.jpg",
    "images/hip2.jpg",
    "images/hip3.jpg"
]

let divContainer = document.getElementById("container");

function renderImg(imgs) {
    let imgsDOM = ""
    for (let i=0; i< imgs.length;i++) {
        imgsDOM += `<img alt="employee in the company" class="team-img" src="${imgs[i]}">`
    }
    divContainer.innerHTML = imgsDOM
}

renderImg(imgs)
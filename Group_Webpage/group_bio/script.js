/**
 * Toggles the display of an individual team member's bio
 * @param {string} bioId - The ID of the bio section to show or hide
 */
function toggleBio(bioId) {
    const bio = document.getElementById(bioId);
    // Toggle between showing and hiding the bio section
    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
    } else {
        bio.style.display = "none";
    }
}

/**
 * Shows the specified section ('bios' or 'vision') and hides the other
 * @param {string} sectionId - The ID of the section to display
 */
function showSection(sectionId) {
    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");
    const contactSection = document.getElementById("contact");
    // Display the bios section and hide the vision section
    if (sectionId === "bios") {
        biosSection.style.display = "flex";
        visionSection.style.display = "none";
        contactSection.style.display = "none";

    }
    // Display the vision section and hide the bios section
    else if (sectionId === "vision") {
        biosSection.style.display = "none";
        visionSection.style.display = "block";
        contactSection.style.display = "block";
    }
}

//Ayden's JS
/**
 * Toggles the display of an individual team member's bio and image
 * @param {string} bioId - The ID of the bio section to show or hide
 * @param {string} imgId - The ID of the image to show or hide
 */
function toggleBioAndImg(bioId, imgId) {
    const bio = document.getElementById(bioId);
    const img = document.getElementById(imgId);
    const div = document.getElementById("A_div")
    const favTools = document.getElementById("FavTools");
    const favToolsList = document.getElementById("FavToolsList");
    const myLinks = document.getElementById("MyLinks");
    const myLinksList = document.getElementById("MyLinksList");
    const button = document.getElementById("A_button");
    // Toggle between showing and hiding elements
    if (bio.style.display === "none" || bio.style.display === "") {

        bio.style.display = "block";
        img.style.display = "inline-block";
        img.style.border = "5px solid darkgreen";
        div.style.backgroundColor = "lightgreen";
        div.style.border = "5px solid darkgreen";
        button.style.backgroundColor = "darkgreen";
        favTools.style.display = "block";
        favToolsList.style.display = "block";
        myLinks.style.display = "block";
        myLinksList.style.display = "block";

    } else {
        bio.style.display = "none";
        img.style.display = "none";
        div.style.backgroundColor = "";
        div.style.border = "";
        favTools.style.display = "none";
        favToolsList.style.display = "none";
        myLinks.style.display = "none";
        myLinksList.style.display = "none";
        button.style.backgroundColor = "";
    }
}
//End Ayden's JS

// Divine's JS
/**
 * Toggles Divine's bio and switches card background to pink
 * @param {string} bioId - The ID of the bio section to show or hide
 * @param {string} cardId - The ID of the card to change background color
 */
function toggleDivineBio(bioId, cardId) {
    const bio = document.getElementById(bioId);
    const card = document.getElementById(cardId);

    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
        card.classList.add("expanded");
    } else {
        bio.style.display = "none";
        card.classList.remove("expanded");
    }
}
// End Divine's JS

// Shyam's JS
function toggleShyamBio(bioId, cardId) {
    const bio = document.getElementById(bioId);
    const card = document.getElementById(cardId);

    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
        card.classList.add("expanded");
    } else {
        bio.style.display = "none";
        card.classList.remove("expanded");
    }
}
// End Shyam's JS
//Deeksha's js
function toggleDeekshaBio(bioId, cardId) {
    const bio = document.getElementById(bioId);
    const card = document.getElementById(cardId);
    const button = card.querySelector('.deeksha-button');

    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";
        card.classList.add("expanded");
        button.textContent = "Hide Bio";

        // Add pulse animation to moodboard icons
        const icons = bio.querySelectorAll('.moodboard-icons img');
        icons.forEach((icon, index) => {
            icon.style.animation = `pulse 0.6s ease ${index * 0.1}s`;
        });
    } else {
        bio.style.display = "none";
        card.classList.remove("expanded");
        button.textContent = "Show Bio";
    }
}
// End Deeksha's Js

// Alejandro's JS
/**
 * Toggles Alejandro's bio, image, favorite tools, and external links.
 * @param {string} bioId - The ID of Alejandro's bio text element.
 * @param {string} imgId - The ID of Alejandro's avatar image element.
 */
function toggleAlejandroBio(bioId, imgId) {
    const bio = document.getElementById(bioId);
    const img = document.getElementById(imgId);
    const tools = document.getElementById("tools-alejandro");
    const links = document.getElementById("links-alejandro");
    const headerTools = document.querySelector("#alejandro-card .tools-section .section-header");
    const headerLinks = document.querySelector("#alejandro-card .links-section .section-header");
    const button = document.querySelector("#alejandro-card .alejandro-button");
    const button1 = document.getElementById("button_alejandro")
    const div = document.getElementById("alejandro-card");
    if (bio.style.display === "none" || bio.style.display === "") {
        div.style.backgroundColor = "darkolivegreen";
        div.style.border = "4px solid black";
        bio.style.display = "block";
        img.style.display = "block";
        tools.style.display = "block";
        links.style.display = "block";
        if (headerTools) headerTools.style.display = "block";
        if (headerLinks) headerLinks.style.display = "block";
        button.textContent = "Hide Bio";
        button1.style.backgroundColor = "black";
        button1.style.color = "darkolivegreen";
        button1.classList.remove("hover-normal");
        button1.classList.add("hover-tan");

    } else {
        div.style.backgroundColor = "white";
        div.style.border = "none";
        bio.style.display = "none";
        img.style.display = "none";
        tools.style.display = "none";
        links.style.display = "none";
        if (headerTools) headerTools.style.display = "none";
        if (headerLinks) headerLinks.style.display = "none";
        button.textContent = "Show Bio";
        button1.style.backgroundColor = "#007BFF";
        button1.style.color = "white";
        button1.classList.remove("hover-tan");
        button1.classList.add("hover-normal");

    }
}
// End Alejandro's JS
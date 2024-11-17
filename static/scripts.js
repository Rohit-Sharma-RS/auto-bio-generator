document.getElementById("temperature").addEventListener("input", function (e) {
    document.getElementById("temperatureValue").innerText = e.target.value;
});

document.getElementById("bioForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const profession = document.getElementById("profession").value;
    const interests = document.getElementById("interests").value;
    const traits = document.getElementById("traits").value;
    const temperature = document.getElementById("temperature").value;
    const about = document.getElementById("about").value;

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            profession,
            interests,
            traits,
            temperature,
            about,
        }),
    });

    const data = await response.json(); // Parse the JSON response

    // Clear any previous results
    const resultContainer = document.getElementById("generatedBio");
    resultContainer.innerHTML = "";

    // Iterate through each bio in the JSON and display it
    Object.keys(data).forEach((key, index) => {
        const bio = data[key];

        const bioCard = document.createElement("div");
        bioCard.classList.add("bio-card");

        const title = document.createElement("h3");
        title.textContent = `Bio ${index + 1}`;

        const content = document.createElement("p");
        content.textContent = bio;

        bioCard.appendChild(title);
        bioCard.appendChild(content);
        resultContainer.appendChild(bioCard);
    });
});

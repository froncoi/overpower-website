function redirectToLogin() {
  window.location.href = "https://discord.com/api/oauth2/authorize?client_id=1090971580357673084&redirect_uri=https%3A%2F%2Fdiscord.gg%2FE4vnewmZ33&response_type=code&scope=email%20guilds.join%20guilds%20identify";
}

const bgAnimation = document.getElementById("bgAnimation");
const numberOfColorBoxes = 400;

for (let i = 0; i < numberOfColorBoxes; i++) {
  const colorBox = document.createElement("div");
  colorBox.classList.add("colorBox");
  bgAnimation.append(colorBox);
}

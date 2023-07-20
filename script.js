function redirectToLogin() {
  // Replace 'YOUR_SERVER_URL' with the URL of your Flask server
  const serverUrl = 'https://discord.gg/E4vnewmZ33';
  const clientId = '1090971580357673084';
  const redirectUri = encodeURIComponent(`${serverUrl}/callback`);

  // Redirect the user to the Discord OAuth2 authorization URL
  window.location.href = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&scope=identify%20guilds%20email`;
}


const bgAnimation = document.getElementById("bgAnimation");
const numberOfColorBoxes = 400;

for (let i = 0; i < numberOfColorBoxes; i++) {
  const colorBox = document.createElement("div");
  colorBox.classList.add("colorBox");
  bgAnimation.append(colorBox);
}

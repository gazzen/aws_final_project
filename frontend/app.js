// API Gateway endpoint URL
const apiUrl = "API_GATEWAY_ENDPOINT_URL";

// Function to fetch all albums
function getAllAlbums() {
  fetch(apiUrl)
    .then((response) => response.json())
    .then((albums) => {
      const albumList = albums
        .map(
          (album) => `
            <div>
                <h3>${album.album_title}</h3>
                <p>Artist: ${album.artist}</p>
                <p>Genre: ${album.genre}</p>
            </div>
        `
        )
        .join("");
      document.getElementById("albums").innerHTML = albumList;
    })
    .catch((error) => console.error("Error fetching albums:", error));
}

// Function to add an album
document
  .getElementById("addAlbumForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const albumData = {
      album_id: Math.random().toString(36).substr(2, 9),
      album_title: formData.get("albumTitle"),
      artist: formData.get("artist"),
      genre: formData.get("genre"),
    };
    fetch(apiUrl, {
      method: "POST",
      body: JSON.stringify(albumData),
    })
      .then((response) => response.json())
      .then((responseData) => {
        console.log("Album added successfully:", responseData);
        getAllAlbums(); // Refresh album list after adding
      })
      .catch((error) => console.error("Error adding album:", error));
  });

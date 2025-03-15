document.getElementById("uploadForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    let fileInput = document.getElementById("pdfFile").files[0];
    let formData = new FormData();
    formData.append("file", fileInput);
    let response = await fetch("/upload", { method: "POST", body: formData });
    let result = await response.json();
    alert(result.message);
});

async function askQuestion() {
    let query = document.getElementById("queryInput").value;
    let response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })
    });
    let result = await response.json();
    document.getElementById("response").innerText = result.answer || result.error;
}

console.log("script loaded");

async function generateSkills() {

    console.log("BUTTON CLICKED");

    const file = document.getElementById("fileInput").files[0];

    console.log("Selected file:", file);

    if (!file) {
        alert("Select a file first");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

        console.log("Starting upload...");

        const uploadResponse = await fetch(
            "http://127.0.0.1:8000/upload",
            {
                method: "POST",
                body: formData
            }
        );

        console.log("Upload response:", uploadResponse);

        const uploadData = await uploadResponse.json();

        console.log("Upload data:", uploadData);

        document.getElementById("result").textContent =
            JSON.stringify(uploadData, null, 2);

    } catch (error) {

        console.error("FULL ERROR:", error);

        document.getElementById("result").textContent =
            error.toString();
    }
}
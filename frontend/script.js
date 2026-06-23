async function generateSkills() {

    const file =
        document.getElementById("fileInput")
        .files[0];

    if (!file) {

        alert("Select a file first");

        return;
    }

    const formData =
        new FormData();

    formData.append("file", file);

    try {

        document.getElementById("result")
            .textContent =
            "Uploading file...";

        // STEP 1

        const uploadResponse =
            await fetch(
                "http://127.0.0.1:8000/upload",
                {
                    method:"POST",
                    body:formData
                }
            );

        const uploadData =
            await uploadResponse.json();

        // STEP 2

        document.getElementById("result")
            .textContent =
            "Generating skills.md...";

        const generateResponse =
            await fetch(
                "http://127.0.0.1:8000/generate-skills",
                {
                    method:"POST",
                    headers:{
                        "Content-Type":
                        "application/json"
                    },
                    body:JSON.stringify({
                        filename:
                        uploadData.filename
                    })
                }
            );

        const generateData =
            await generateResponse.json();

        // STEP 3

        const fileName =
            generateData.skills_file;

        const downloadUrl =
            "http://127.0.0.1:8000/download/"
            + fileName;

        const fileResponse =
            await fetch(downloadUrl);

        const skillsText =
            await fileResponse.text();

        document.getElementById("result")
            .textContent =
            skillsText;

        const link =
            document.getElementById(
                "downloadLink"
            );

        link.href =
            downloadUrl;

        link.style.display =
            "inline-block";

    }

    catch(error){

        console.error(error);

        document.getElementById(
            "result"
        ).textContent =
        "Error generating skills.";
    }
}
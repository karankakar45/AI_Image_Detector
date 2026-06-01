const imageInput =
document.getElementById("imageInput");

const preview =
document.getElementById("preview");

imageInput.addEventListener("change",()=>{

    const file =
    imageInput.files[0];

    if(file){

        preview.src =
        URL.createObjectURL(file);

        preview.style.display="block";
    }

});

document
.getElementById("detectBtn")
.addEventListener("click",async()=>{

    const file =
    imageInput.files[0];

    if(!file){
        alert("Select an image first");
        return;
    }

    const loader =
    document.getElementById("loader");

    loader.style.display="block";

    const formData =
    new FormData();

    formData.append("file",file);

    try {
        const response =
        await fetch(
          "http://localhost:8000/predict",
          {
            method:"POST",
            body:formData
          }
        );

        if (!response.ok) {
            throw new Error("Failed to analyze image");
        }

        const data =
        await response.json();

        loader.style.display="none";

        document
        .getElementById("resultCard")
        .style.display="block";

        document
        .getElementById("result")
        .innerText =
        data.prediction;

        document
        .getElementById("confidence")
        .innerText =
        `Confidence: ${data.confidence}%`;
    } catch (error) {
        loader.style.display="none";
        alert("Error analyzing image: " + error.message);
    }
});
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

imageInput.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        reader.addEventListener("load", function () {
            preview.setAttribute("src", this.result);
            preview.style.display = "block";
        });

        reader.readAsDataURL(file);
    }
});

async function uploadImage() {

    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    const response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `Prediction: ${data.prediction}<br>
         Confidence: ${data.confidence}%`;
}
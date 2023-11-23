function copyToClipboard() {
    // Create a new textarea element and set its value to the generated business plan content
    var textArea = document.createElement("textarea");
    textArea.value = document.body.innerText;

    // Append the textarea to the document
    document.body.appendChild(textArea);

    // Select the content of the textarea
    textArea.select();

    try {
        // Copy the selected text to the clipboard using the Clipboard API
        document.execCommand('copy');
        // Alert the user that the content has been copied (you can customize this part)
        alert("Business plan copied to clipboard!");
    } catch (err) {
        // Handle any errors that may occur during copying
        console.error('Unable to copy to clipboard', err);
    } finally {
        // Remove the textarea from the document
        document.body.removeChild(textArea);
    }
}

// Attach the copyToClipboard function to the button click event
document.getElementById("copyButton").addEventListener("click", copyToClipboard);



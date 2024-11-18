// new window.IntaSend({
//     publicAPIKey: "ISPubKey_test_8f1e16f4-5c53-4618-a00b-d039dc7166a3",
//     live: false //set to true when going live
//     })
//     .on("COMPLETE", (results) => {console.log("Do something on success", results)})
//     .on("FAILED", (results) => {console.log("Do something on failure", results)})
//     .on("IN-PROGRESS", (results) => {console.log("Payment in progress status", results)})
  

document.getElementById("payButton").addEventListener("click", () => {
    const movieSelect = document.getElementById("movie");
    const selectedMovie = movieSelect.options[movieSelect.selectedIndex].text;
    const amount = movieSelect.value;
  
    // IntaSend Payment API
    const paymentData = {
      api_key: "ISPubKey_test_8f1e16f4-5c53-4618-a00b-d039dc7166a3", // Replace with your IntaSend API Key
      amount: amount,
      currency: "KES",
      email: "customer@example.com",
      first_name: "John",
      last_name: "Doe",
      phone_number: "+254712345678",
      description: `Payment for ${selectedMovie}`,
      callback_url: "https://your-website.com/callback", // Replace with your callback URL
      redirect_url: "https://your-website.com/thank-you", // Replace with your redirect URL
    };
  
    // POST request to IntaSend
    fetch("https://api.intasend.com/v1/checkout/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(paymentData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.checkout_url) {
          // Redirect user to payment page
          window.location.href = data.checkout_url;
        } else {
          alert("Failed to initiate payment. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
      });
  });
  
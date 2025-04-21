document.getElementById("spinForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const wheel = document.getElementById("wheel");
    const resultBox = document.getElementById("result");

    const discounts = [10, 20, 50];
    const randomIndex = Math.floor(Math.random() * discounts.length);
    const selected = discounts[randomIndex];

    const degrees = 3600 + randomIndex * 120 + Math.floor(Math.random() * 60);
    wheel.style.transform = `rotate(${degrees}deg)`;

    setTimeout(() => {
        resultBox.style.display = "block";
        resultBox.innerHTML = `🎉 مبروك! حصلت على خصم ${selected}%`;
    }, 5000);
});

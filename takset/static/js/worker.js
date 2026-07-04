const input = document.getElementById("search");
const results = document.getElementById("results");

input.addEventListener("input", function () {
  let query = this.value;

  if (query.length === 0) {
    results.innerHTML = "";
    return;
  }

  fetch(`/api/workers/?q=${query}`)
    .then((res) => res.json())
    .then((data) => {
      results.innerHTML = "";

      data.forEach((worker) => {
        let li = document.createElement("li");
        li.textContent = worker.name;

        li.onclick = function () {
          input.value = worker.name;
          results.innerHTML = "";
        };

        results.appendChild(li);
      });
    });
});

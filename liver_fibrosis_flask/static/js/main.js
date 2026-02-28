(function () {
  const imgInput = document.getElementById("imageInput");
  const preview = document.getElementById("imagePreview");
  const previewWrap = document.getElementById("previewWrap");
  const predictForm = document.getElementById("predictForm");
  const submitBtn = document.getElementById("submitBtn");
  const spinner = document.getElementById("spinner");

  if (imgInput && preview && previewWrap) {
    imgInput.addEventListener("change", (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file) return;
      const url = URL.createObjectURL(file);
      preview.src = url;
      previewWrap.classList.remove("hidden");
    });
  }

  if (predictForm && submitBtn) {
    predictForm.addEventListener("submit", () => {
      submitBtn.disabled = true;
      submitBtn.classList.add("opacity-70", "cursor-not-allowed");
      if (spinner) spinner.classList.remove("hidden");
    });
  }

  const search = document.getElementById("historySearch");
  const table = document.getElementById("historyTable");
  if (search && table) {
    search.addEventListener("input", () => {
      const q = search.value.trim().toLowerCase();
      const rows = table.querySelectorAll("tbody tr");
      rows.forEach((tr) => {
        const txt = tr.innerText.toLowerCase();
        tr.style.display = txt.includes(q) ? "" : "none";
      });
    });
  }

  const flash = document.getElementById("flashWrap");
  if (flash) {
    setTimeout(() => {
      flash.classList.add("opacity-0");
      setTimeout(() => flash.remove(), 350);
    }, 3500);
  }
})();
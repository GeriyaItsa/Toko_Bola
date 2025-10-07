function showToast(message, type = "success") {
  // type bisa 'success', 'error', atau 'info'
  const existingToast = document.getElementById("toast-notification");
  if (existingToast) existingToast.remove();

  const toast = document.createElement("div");
  toast.id = "toast-notification";
  toast.className = `
    fixed top-5 right-5 px-4 py-3 rounded-xl shadow-lg text-white
    ${type === "success" ? "bg-green-500" : type === "error" ? "bg-red-500" : "bg-blue-500"}
    transition-opacity duration-300 opacity-0 z-50
  `;
  toast.textContent = message;
  document.body.appendChild(toast);

  // animasi muncul
  setTimeout(() => (toast.style.opacity = "1"), 50);

  // hilang setelah 3 detik
  setTimeout(() => {
    toast.style.opacity = "0";
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

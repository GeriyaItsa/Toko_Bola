document.addEventListener("DOMContentLoaded", () => {
  const refreshBtn = document.getElementById("refreshButton");
  const productList = document.getElementById("product-list");

  refreshBtn.addEventListener("click", async () => {
    refreshBtn.disabled = true;
    refreshBtn.textContent = "Memuat...";

    try {
      const response = await fetch("/json/");
      if (!response.ok) throw new Error("Gagal mengambil data");

      const data = await response.json();

      // Kosongkan isi lama
      productList.innerHTML = "";

      // Isi ulang dengan produk terbaru
      data.forEach((product) => {
        const card = document.createElement("div");
        card.className =
          "bg-white rounded-xl shadow p-4 hover:shadow-md transition";

        card.innerHTML = `
          <img src="${product.thumbnail || '/static/images/default.png'}" 
               alt="${product.name}" 
               class="w-full h-40 object-cover rounded-md mb-2">
          <h3 class="font-semibold">${product.name}</h3>
          <p class="text-sm text-gray-500">${product.category}</p>
          <p class="text-blue-600 font-semibold mt-1">Rp${product.price}</p>
        `;

        productList.appendChild(card);
      });

      showToast("Daftar produk berhasil diperbarui!", "success");
    } catch (error) {
      console.error(error);
      showToast("Gagal memuat produk terbaru!", "error");
    } finally {
      refreshBtn.disabled = false;
      refreshBtn.textContent = "🔄 Refresh";
    }
  });
});

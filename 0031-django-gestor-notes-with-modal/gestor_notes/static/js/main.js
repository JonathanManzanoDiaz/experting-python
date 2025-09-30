const modal = document.getElementById("noteModal");
const closeBtn = document.getElementById("closeModal");
const form = document.getElementById("noteForm");
const submitBtn = document.getElementById("submitBtn");

// --- Abrir modal en modo EDITAR ---
document.querySelectorAll(".open-modal").forEach(button => {
  button.addEventListener("click", () => {
    document.getElementById("modalNoteId").value = button.dataset.id;
    document.getElementById("modalTitle").value = button.dataset.title;
    document.getElementById("modalContent").value = button.dataset.content;

    // Ajustar formulario para EDITAR
    form.action = "/notes/update/";  // o {% url 'update_note' %} si lo inyectas desde template
    submitBtn.textContent = "Guardar cambios";

    modal.style.display = "flex"; // mostrar modal
  });
});

// --- Abrir modal en modo CREAR ---
const createBtn = document.getElementById("createNoteBtn");
if (createBtn) {
  createBtn.addEventListener("click", (e) => {
    e.preventDefault(); // evita recargar la página
    document.getElementById("modalNoteId").value = "";
    document.getElementById("modalTitle").value = "";
    document.getElementById("modalContent").value = "";

    // Ajustar formulario para CREAR
    form.action = "/notes/create/";  // o {% url 'create_note' %}
    submitBtn.textContent = "Crear";

    modal.style.display = "flex"; // mostrar modal
  });
}

// --- Cerrar modal ---
closeBtn.onclick = () => modal.style.display = "none";
window.onclick = (e) => {
  if (e.target === modal) modal.style.display = "none";
};

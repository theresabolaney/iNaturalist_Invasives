document.forms.taxonToStatus.addEventListener("submit", submitTaxonToStatus);

function submitTaxonToStatus(event) {
  event.preventDefault();
  const form = event.target;
  const taxonId = form.elements.taxonId;
  const output = form.elements.regulationStatus;

  output.textContent =
    `Form submitted: taxonToStatus; taxonId=${taxonId.value}\n` +
    `GET ${form.action}/${taxonId.value}`;
}

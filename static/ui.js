document.forms.taxonToStatus.addEventListener("submit", submitTaxonToStatus);

async function submitTaxonToStatus(event) {
  event.preventDefault();
  const form = event.target;
  const taxonId = form.elements.taxonId;
  const output = form.elements.regulationStatus;

  const url = `${form.action}/${taxonId.value}`;

  output.textContent =
    `Form submitted: taxonToStatus; taxonId=${taxonId.value}\n` +
    `GET ${url}\n`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.text();
    console.log(result);
    output.textContent += result;
  } catch (error) {
    console.error(error.message);
  }
}

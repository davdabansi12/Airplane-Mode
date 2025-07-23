frappe.ready(() => {
    const website = frappe.web_form.get_value("website");

    if (website) {
        const link_html = `<div class="website-link">
            <a href="${website}" target="_blank" rel="noopener noreferrer" style="font-weight: bold; color: #1a73e8;">
                Visit Official Website ✈️
            </a>
        </div>`;

        // Append after the form
        const wrapper = document.createElement('div');
        wrapper.innerHTML = link_html;
        document.querySelector(".web-form-container").appendChild(wrapper);
    }
});
// Copyright (c) 2025, bansi davda and contributors
// For license information, please see license.txt


frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        frm.clear_custom_buttons();

        if (!frm.is_new() && frm.doc.website) {
            frm.add_custom_button(__('Visit Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
        }
    }
});

odoo.define('pos_lock_mode.lock_mode', function (require) {
    "use strict";

    var core = require('web.core');
    var QWeb = core.qweb;
    var _t = core._t;
    var screens = require('point_of_sale.screens');
    var NumpadWidget = screens.NumpadWidget;

    NumpadWidget.include({
        clickChangeMode: function (event) {
            var self = this;
            var mode = self.state.get('mode');
            var newMode = event.currentTarget.attributes['data-mode'].nodeValue;
            if (mode == newMode) {
                return self.state.changeMode(newMode);
            }
            if (newMode == 'discount') {
                if (self.pos.config.lock_discount == true) {
                    self.gui.show_popup('password', {
                        'title': _t('Password ?'),
                        confirm: function (pw) {
                            if (pw !== self.pos.config.discount_password) {
                                self.gui.show_popup('error', {
                                    'title': _t('Error'),
                                    'body': _t('Incorrect password. Please try again'),
                                });
                            } else {
                                return self.state.changeMode(newMode);
                            }
                        },
                    });
                } else {
                    return self.state.changeMode(newMode);
                }
            } else if (newMode == 'price') {
                if (self.pos.config.lock_price == true) {
                    self.gui.show_popup('password', {
                        'title': _t('Password ?'),
                        confirm: function (pw) {
                            if (pw !== self.pos.config.price_password) {
                                self.gui.show_popup('error', {
                                    'title': _t('Error'),
                                    'body': _t('Incorrect password. Please try again'),
                                });
                            } else {
                                return self.state.changeMode(newMode);
                            }
                        },
                    });
                } else {
                    return self.state.changeMode(newMode);
                }
            } else {
                return self.state.changeMode(newMode);
            }
        },
    });

});
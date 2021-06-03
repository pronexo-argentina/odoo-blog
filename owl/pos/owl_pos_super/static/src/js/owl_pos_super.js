odoo.define('owl_pos_super.TicketScreen_Popup', function(require) {
   'use strict';
   const Registries = require('point_of_sale.Registries');
   const TicketScreen = require('point_of_sale.TicketScreen');
   const { posbus } = require('point_of_sale.utils');



const PosTicketScreen = (TicketScreen) =>
class extends TicketScreen {
    async deleteOrder(order) {
    const screen = order.get_screen_data();
    if (['ProductScreen', 'PaymentScreen'].includes(screen.name) && order.get_orderlines().length > 0) {
        const { confirmed } = await this.showPopup('ConfirmPopup', {
            title: 'Líneas de pedido existentes',
            body: `¿Está seguro de que quiere eliminar el ticket ${order.name}?`
        });
        if (!confirmed) return;
    }
    if (order) {
        order.destroy({ reason: 'abandon' });
    }
    posbus.trigger('order-deleted');
}
};

   Registries.Component.extend(TicketScreen, PosTicketScreen);
   return TicketScreen;

});
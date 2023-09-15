import './assets/foundation.min.css'

import { createApp } from 'vue'
import { createStore } from 'vuex';

import App from './App.vue'
import router from './router'

const store = createStore({
    state: {
        mode: 'JoinCreate.Welcome',
        hand: [{
            card: 'AS',
            selected: false
        }, {
            card: 'QD',
            selected: false
        }, {
            card: '8H',
            selected: false
        }],
        players: ['Sarah', 'Paul', 'Sara']
    },
    mutations: {
        CHANGE_VIEW(state, payload) {
            state.mode = payload;
        },
        TOGGLE_CARD(state, payload) {
            state.hand = state.hand.map((c, i) => {
                if (payload.index === i && payload.card == c.card) {
                    return { card: c.card, selected: !c.selected };
                }
                return c;
            });
        },
    },
    actions: {
        changeView(context, payload) {
            context.commit('CHANGE_VIEW', payload);
        },
        toggleCard(context, payload) {
            context.commit('TOGGLE_CARD', payload);
        },
    },
});

const app = createApp(App)

app.use(store);
//app.use(router)

app.mount('#app')

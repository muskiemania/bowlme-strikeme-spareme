import './assets/foundation.min.css'

import { createApp } from 'vue'
import { createStore } from 'vuex';

import App from './App.vue'
import router from './router'

const store = createStore({
    state: {
        mode: 'JoinCreate.Welcome',
        playerName: '',
        playerId: '',
        gameId: '',
        token: '',
        isHost: false,
        hand: [],
        players: ['Sarah', 'Paul', 'Sara']
    },
    mutations: {
        CHANGE_VIEW(state, payload) {
            state.mode = payload;
        },
        DRAW_CARDS(state, payload) {
            state.hand = payload.map((card) => {
                return { card: card, selected: false };
            });
        },
        STORE_GAME_INFO(state, payload) {
            state.playerName = payload.playerName;
            state.playerId = payload.playerId;
            state.gameId = payload.gameId;
            state.isHost = payload.isHost;
            state.token = payload.token;

            console.log(`token: ${state.token}`);
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
        drawCards(context, payload) {
            context.commit('DRAW_CARDS', payload);
        },
        storeGameInfo(context, payload) {
            context.commit('STORE_GAME_INFO', payload);
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

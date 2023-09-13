import './assets/foundation.min.css'

import { createApp } from 'vue'
import { createStore } from 'vuex';

import App from './App.vue'
import router from './router'

const store = createStore({
    state: {
        mode: 'JoinCreate.Welcome'
    },
    mutations: {
        CHANGE_VIEW(state, payload) {
            state.mode = payload;
        },
    },
    actions: {
        changeView(context, payload) {
            context.commit('CHANGE_VIEW', payload);
        },
    },
});

const app = createApp(App)

app.use(store);
//app.use(router)

app.mount('#app')

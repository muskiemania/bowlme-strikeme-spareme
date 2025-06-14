import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStartHereStore = defineStore('startHere', {

    state: () => {
        return {
            seriesDate: ref('')
        };
    },
    getters: {
        getSeriesDate: (state) => state.seriesDate,
    },
    actions: {
        setDate(t) {
            console.log(t);
            this.seriesDate = t;
        }
    }
});

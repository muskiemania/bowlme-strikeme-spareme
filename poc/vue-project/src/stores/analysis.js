import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAnalysisStore = defineStore('analysis', {

    state: () => {
        return {
            pinsActive: ref(false),
            pinsClick: ref(new Set()),
            pinsText: ref(''),

            pinsExit: ref(0),
            pinsEnter: ref(0),
            breakPoint: ref(0),
            breakDistance: ref(0),
            arrows: ref(0),
            slide: ref(0),
            start: ref(0)

        };
    },
    getters: {
        getPinsActive: (state) => state.pinsActive,
        //getPins: (state, p) => state,
        getPinsClicked: (state) =>  state.pinsClick,
    },
    actions: {
        usePins() {
            this.pinsActive = true;
            this.pinsClick.clear();
            this.pinsText = ''
        },
        spare() {
            this.pinsActive = false;
            this.pinsClick.clear();
            this.pinsText = '/';
        },
        strike() {
            this.pinsActive = false;
            this.pinsClick.clear();
            this.pinsText = 'X';
        },
        pins(p) {
            this.pinsActive = true;
            this.pinsText = '';
            if (!this.pinsClick.has(p))
                this.pinsClick.add(p);
            else
                this.pinsClick.delete(p);
        },
        pinText(t) {
            this.pinsActive = false;
            this.pinsClick.clear();
            this.pinsText = t;
        }
    }
});

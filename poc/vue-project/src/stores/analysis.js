import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAnalysisStore = defineStore('analysis', {

    state: () => {
        return {
            pinsActive: ref(false),
            pinsClick: ref(new Set()),
            pinsText: ref(''),

            pinExit: ref(0),
            pinEnter: ref(0),
            breakPoint: ref(0),
            breakDistance: ref(0),
            arrows: ref(0),
            slide: ref(0),
            startDots: ref(0),
            startDistance: ref(0),

            pexOn: ref(true),
            penOn: ref(true),
            breakPtOn: ref(true),
            breakDistOn: ref(true),
            arrowsOn: ref(true),
            slideOn: ref(true),
            startDotsOn: ref(true),
            startDistOn: ref(true)
        };
    },
    getters: {
        getPinsActive: (state) => state.pinsActive,
        //getPins: (state, p) => state,
        getPinsClicked: (state) =>  state.pinsClick,
        
        anyAnalysis: (state) => {
            return (state.pexOn || state.penOn || state.breakPtOn || state.breakDistOn || state.arrowsOn || state.slideOn || state.startDotsOn || state.startDistOn);
        }
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
        },
        toggleAnalysis(a) {
            if (a === 1) {
                this.pexOn = !this.pexOn;
            }
            if (a === 2) {
                this.penOn = !this.penOn;
            }
            if (a === 3) {
                this.breakPtOn = !this.breakPtOn;
            }
            if (a === 4) {
                this.breakDistOn = !this.breakDistOn;
            }
            if (a === 5) {
                this.arrowsOn = !this.arrowsOn;
            }
            if (a === 6) {
                this.slideOn = !this.slideOn;
            }
            if (a === 7) {
                this.startDotsOn = !this.startDotsOn;
            }
            if (a === 8) {
                this.startDistOn = !this.startDistOn;
            }
        },
        setAnalysis(a, b) {
            if (a === 1) {
                this.pinExit = b;
            }
            if (a === 2) {
                this.pinEnter = b;
            }
            if (a === 3) {
                this.breakPoint = b;
            }
            if (a === 4) {
                this.breakDistance = b;
            }
            if (a === 5) {
                this.arrows = b;
            }
            if (a === 6) {
                this.slide = b;
            }
            if (a === 7) {
                this.startDots = b;
            }
            if (a === 8) {
                this.startDistance = b;
            }
        }
 
    }
});

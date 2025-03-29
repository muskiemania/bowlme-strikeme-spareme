import { ref, computed, toRaw } from 'vue'
import { defineStore } from 'pinia'

export const useDisplayStore = defineStore('display', {

    state: () => {
        return {
            sliderOpen: ref(false),

            gameNumber: 1,
            //frameLeft: ref(false),
            //frameRight: ref(false),
            frameNumber: 1,
            //throw1: ref(0),
            //throw2: ref(0),
            //throw3: ref(0),
            analysisCursor: ref(0),
            analysis1: ref(''),
            analysis2: ref(''),
            analysis3: ref(''),
            master: ref({
                games: [1,2,3],
                gameData: {
                    "1": {
                        "frames": [
                            {
                                "frameNumber": 1,
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "7"
                                    },
                                    {
                                        "pins": "/"
                                    }
                                ],
                                "totalScore": 18
                            },
                            {
                                "frameNumber": 2,
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "8"
                                    },
                                    {
                                        "pins": "1"
                                    }
                                ],
                                "totalScore": 27
                            },
                            {
                                "frameNumber": 3,
                                "throws": [
                                    {
                                        "id": "b",
                                        "pins": "X"
                                    },
                                ],
                                "totalScore": ""
                            },
                        ],
                        "analysis": {
                            "a": {
                                "url": "https://dbeusqqg6817d.cloudfront.net/muskiemania/abc123_1_7c314aca36b2.png"
                            },
                            "b": {
                                "url": "https://dbeusqqg6817d.cloudfront.net/muskiemania/xyz123_1_7e6976d9bebe.png"
                            }
                        }
                    },
                    "2": {
                    },
                    "3": {
                    }
                }
            })
        };
    },
    getters: {
    
        getGameNumber: (state) => state.gameNumber,
        getGameLeft: (state) => state.gameNumber > 1,
        getGameRight: (state) => state.gameNumber === Math.max(state.master.games),
        getFrameNumber: (state) => state.frameNumber,
        getTotalFrames: (state) => { 
            return state.master.gameData[state.gameNumber.toString()].frames.map((e) => e.frameNumber);
        },
        getFrameThrows: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frameNumber === state.frameNumber);
            return f['throws'].map((e) => e['pins']);
        },
        getFrameScore: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frameNumber === state.frameNumber);
            return f.totalScore
        },
        getSliderIsOpen: (state) => state.sliderOpen,
        getAnalysis: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frameNumber === state.frameNumber);
            const t = f['throws'].map((e) => e['id']).filter(value => value !== undefined);

            //return toRaw(f);

            let u = [];
            t.forEach((i) => {
                const a = state.master.gameData[state.gameNumber.toString()].analysis || {};
                if (i in a) {
                    u.push(a[i].url)
                }
            });
            return u;
        },
        getMaster: (state) => state.master
    },
    actions: {
        toggleSlider() {
            this.sliderOpen = !this.sliderOpen            
        },
        nextFrame() {
            this.frameNumber++
        },
        previousFrame() {
            this.frameNumber--
        },
    }
});


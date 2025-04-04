import { ref, computed, toRaw } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useDisplayStore = defineStore('display', {

    state: () => {
        return {
            loading: ref(true),
            sliderOpen: ref(false),

            gameNumber: 1,
            frameNumber: 1,
            analysisCursor: ref(0),
            master: ref({
                games: [1,2,3],
                gameData: {
                    "1": {
                        "frames": [
                            {
                                "frame": "1",
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "7"
                                    },
                                    {
                                        "pins": "/"
                                    }
                                ],
                                "total": 18
                            },
                            {
                                "frame": "2",
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "8"
                                    },
                                    {
                                        "pins": "1"
                                    }
                                ],
                                "total": 27
                            },
                            {
                                "frame": "3",
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
   
        isLoading: (state) => state.loading,
        getGameNumber: (state) => state.gameNumber,
        getGameLeft: (state) => state.gameNumber > 1,
        getGameRight: (state) => state.gameNumber === Math.max(state.master.games),
        getFrameNumber: (state) => state.frameNumber,
        getTotalFrames: (state) => { 
            return state.master.gameData[state.gameNumber.toString()].frames.map((e) => e.frame);
        },
        getFrameThrows: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames;
            const fr = f.find((e) => e.frame === state.frameNumber.toString());
            console.log(state.frameNumber);
            console.log(fr);

            return fr['throws'].map((e) => e['pins']);
        },
        getFrameScore: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frame === state.frameNumber.toString());
            return f.total
        },
        getSliderIsOpen: (state) => state.sliderOpen,
        getAnalysis: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frame === state.frameNumber.toString());
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
        getSeries(seriesId) {
            
            const BASE_URL = 'https://smqu6xcne4.execute-api.us-west-2.amazonaws.com';

            // must call out to API to retrieve series
            // then initialize
            // finally set loading ==> false
            axios.get(`${BASE_URL}/series/${seriesId}`)
            .then((reply) => {
                
                const master = {};
                master.games = reply.data.games;
                master.gameData = reply.data.game_data;

                const current = Math.max(...reply.data.games)
                const frames = master.gameData[current.toString()].frames.map((e) => e.frame);

                const thisFrame = Math.max(...frames);

                this.master = master;
                this.frameNumber = parseInt(thisFrame);
                this.gameNumber = parseInt(current);
                this.loading = false;
            })
            .catch((error) => {
                console.log(error);
            });

        }
    }
});


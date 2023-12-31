import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const follow = {
  plugins:[
    createPersistedState()
  ],
  state: {
    // user_id : this.$store.state.user.id,
    follow : []
  },
  getters: {
    GET_FOLLOW(state, res){
      state.follow = res
    }
  },
  mutations: {
  },
  actions: {
    getFollow(context){
      axios({
        method:'get',
        url : `${API_URL}/accounts/follow/:user_id`

      })
      .then((res)=>{
        console.log(res, 'follow res')
        context.commit('GET_FOLLOW')
      })
      .catch((err)=>{
        console.log(err, 'followerr')
      })
    }
  },
  modules: {
  }
}


export default follow
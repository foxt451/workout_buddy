import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";
import * as fs
from "https://www.gstatic.com/firebasejs/9.6.10/firebase-firestore.js";

const firebaseConfig = {

    apiKey: "AIzaSyBlCF1MRhwG7JHA9-SuSUQLiaQXCqPj9rM",
    authDomain: "workoutbuddy-70091.firebaseapp.com",
    projectId: "workoutbuddy-70091",
    storageBucket: "workoutbuddy-70091.appspot.com",
    messagingSenderId: "102463363442",
    appId: "1:102463363442:web:16d6528bb454b17259a5eb"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = fs.getFirestore(app);

const userFrom = JSON.parse(document.getElementById('user-from').textContent).id;
const userTo = JSON.parse(document.getElementById('user-to').textContent).id;

const userFromName = JSON.parse(document.getElementById('user-from').textContent).username;
const userToName = JSON.parse(document.getElementById('user-to').textContent).username;

const userFromLink = JSON.parse(document.getElementById('user-from').textContent).userlink;
const userToLink = JSON.parse(document.getElementById('user-to').textContent).userlink;

const chatList = document.querySelector('#chat-list');

const html = (username, userlink, msg, dateNormal) => `
    <li class="list-group-item">
        <a class="text-primary username" href="${userlink}">${_.escape(username)}</a>
        <br>
        <span class="message">${_.escape(msg)}</span>
        <div class="time text-muted">${dateFns.formatDistanceToNow(dateNormal)} ago</div>
    </li>
    `;

function clearList() {
    chatList.innerHTML = '';
}

function addChat(doc) {
    chatList.innerHTML += html(...(doc.userFrom === userFrom ? [userFromName, userFromLink] : [userToName, userToLink]), doc.message, doc.created_at.toDate());
}

const onSnapshot = snapshot => {
    clearList();
    snapshot.forEach(doc => {
        addChat(doc.data());
    });
}
messages = fs.collection(db, 'messages');
const unsub = fs.onSnapshot(fs.query(messages, fs.orderBy('created_at'), fs.where('userTo', '==', user), fs.where('userFrom', '==', user)), onSnapshot);
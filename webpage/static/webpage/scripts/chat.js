import * as fs
from "https://www.gstatic.com/firebasejs/9.6.10/firebase-firestore.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration

export class ChatSession {
    // userFrom and userTo are user ids
    constructor(db, userFrom, userTo) {
        this.db = db;
        this.userFrom = userFrom;
        this.userTo = userTo;
        this.messages = fs.collection(this.db, 'messages');
    }

    async sendMessage(message) {
        const now = new Date();
        const doc = {
            created_at: fs.Timestamp.fromDate(now),
            message,
            userTo: this.userTo,
            userFrom: this.userFrom,
        };
        const response = await fs.addDoc(this.messages, doc);
        return response
    }

    getMessages(onAdded) {
        const onSnapshot = snapshot => {
            snapshot.docChanges().forEach(change => {
                if (change.type == "added") {
                    onAdded(change.doc.data())
                }
            });
        }
        const unsub1 = fs.onSnapshot(fs.query(this.messages, fs.orderBy('created_at'), fs.where('userTo', '==', this.userTo), fs.where('userFrom', '==', this.userFrom)), onSnapshot);
        // replies
        const unsub2 = fs.onSnapshot(fs.query(this.messages, fs.orderBy('created_at'), fs.where('userTo', '==', this.userFrom), fs.where('userFrom', '==', this.userTo)), onSnapshot);
        this.unsub = () => { unsub1(); unsub2(); };
    }
}
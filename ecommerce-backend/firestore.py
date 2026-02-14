import os
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "serviceAccountKey.json"))
firebase_admin.initialize_app(cred, {
    "projectId": os.getenv("FIREBASE_PROJECT_ID", "react-deploy-d9306")
})

# Firestore client
db = firestore.client()


# --------------- Helper Functions ---------------

def get_document(collection: str, doc_id: str) -> dict | None:
    """Fetch a single document by its ID."""
    doc_ref = db.collection(collection).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        data["id"] = doc.id
        return data
    return None


def get_all_documents(collection: str) -> list[dict]:
    """Fetch all documents from a collection."""
    docs = db.collection(collection).stream()
    results = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        results.append(data)
    return results


def query_documents(collection: str, field: str, operator: str, value) -> list[dict]:
    """Query documents by a single field condition."""
    docs = db.collection(collection).where(field, operator, value).stream()
    results = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        results.append(data)
    return results


def add_document(collection: str, data: dict, doc_id: str = None) -> str:
    """Add a document. If doc_id is provided, use it as the document ID; otherwise auto-generate."""
    if doc_id:
        db.collection(collection).document(doc_id).set(data)
        return doc_id
    else:
        _, doc_ref = db.collection(collection).add(data)
        return doc_ref.id


def update_document(collection: str, doc_id: str, data: dict) -> None:
    """Update fields on an existing document."""
    db.collection(collection).document(doc_id).update(data)


def delete_document(collection: str, doc_id: str) -> None:
    """Delete a document by its ID."""
    db.collection(collection).document(doc_id).delete()

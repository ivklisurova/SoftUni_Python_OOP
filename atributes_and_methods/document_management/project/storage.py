class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        ctg = [c for c in self.categories if c.id == category_id][0]
        ctg.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        tpc = [t for t in self.topics if t.id == topic_id][0]
        tpc.topic = new_topic
        tpc.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        ctg = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(ctg)

    def delete_topic(self, topic_id):
        tpc = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(tpc)

    def delete_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(doc)

    def get_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id][0]
        return doc.__repr__()

    def __repr__(self):
        for doc in self.documents:
            return f'{doc.__repr__()}\n'


# from atributes_and_methods.document_management.category import Category
# from atributes_and_methods.document_management.document import Document
# from atributes_and_methods.document_management.topic import Topic


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)

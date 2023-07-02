class SubjectKnowledge:
    def __init__(self):
        self.knowledge_base = {}

    def add_topic(self, topic, information):
        """
        Add information about a specific topic to the knowledge base.
        """
        if topic not in self.knowledge_base:
            self.knowledge_base[topic] = []

        self.knowledge_base[topic].append(information)

    def get_topic_information(self, topic):
        """
        Retrieve information about a specific topic from the knowledge base.
        """
        if topic in self.knowledge_base:
            return self.knowledge_base[topic]
        else:
            return None

    def get_related_topics(self, topic):
        """
        Retrieve a list of related topics based on the given topic.
        """
        related_topics = []

        # Implement your logic to determine related topics based on the given topic

        return related_topics


# Usage example
knowledge = SubjectKnowledge()

# Adding information to the knowledge base
knowledge.add_topic("Science", "The study of the physical and natural world.")
knowledge.add_topic("Science", "It involves observation, experimentation, and analysis.")
knowledge.add_topic("Mathematics", "The study of numbers, shapes, and patterns.")
knowledge.add_topic("Mathematics", "It provides a framework for logical and critical thinking.")

# Retrieving information from the knowledge base
science_info = knowledge.get_topic_information("Science")
if science_info:
    for info in science_info:
        print(info)

related_topics = knowledge.get_related_topics("Mathematics")
print(related_topics)

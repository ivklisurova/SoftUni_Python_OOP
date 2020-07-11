class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer_id = subscription.customer_id
        customer = [c for c in self.customers if c.id == customer_id][0]
        trainer_id = subscription.trainer_id
        trainer = [t for t in self.trainers if t.id == trainer_id][0]
        plan_id = subscription.exercise_id
        plan = [p for p in self.plans if p.id == plan_id][0]
        equipment_id = plan.equipment_id
        equipment = [e for e in self.equipment if e.id == equipment_id][0]

        result = subscription.__repr__() + '\n'
        result += customer.__repr__() + '\n'
        result += trainer.__repr__() + '\n'
        result += equipment.__repr__() + '\n'
        result += plan.__repr__()
        return result


# from atributes_and_methods.gym.project.customer import Customer
# from atributes_and_methods.gym.project.equipment import Equipment
# from atributes_and_methods.gym.project.trainer import Trainer
# from atributes_and_methods.gym.project.subscription import Subscription
# from atributes_and_methods.gym.project.exercise_plan import ExercisePlan
#
# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
# plan2 = ExercisePlan.from_hours(22, 2, 2)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_plan(plan2)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))

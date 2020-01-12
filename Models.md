# Always plan your models before Starting
Model Architere planning

MembershipModel
    -slug 
    -type(free,pro,enterprise)
    -price
    -stripe_plan_id


UserMembership
    -user (foreignKey to default user)
    -stripe_custom_id
    -membership_type (foreignKey to default MemberShip)

Subscription
    -user_membership
    -stripe_subscription_id (foreignKey to default UserMemberShip)
    -active
Course
    -slug
    -title
    -description
    -allowed_memberships (foreignKey to default MemberShip)
Lesson
    -slug 
    -title
    -course (foreignKey to default Course)
    -position
    -video
    -thumbnail


from marshmallow import fields
from flask.ext.restful import marshal, request
from humanoid.joints import HingeJoint, HingeJointSerializer


class Elbow(HingeJoint):
    """
    Elbow extends the basic hinge joint class and
    sets a limit to its range of movement.
    """

    def __init__(self):
        super(Elbow, self).__init__()

        # Limits = [lower, upper]
        self.data["limits"] = [0, 50]

        self.parent_id = None

        self.data["href"] = "/api/robot/body/arms/" + str(self.parent_id) + "/elbow/"

    def set_parent_id(self, uuid):
        self.parent_id = uuid
        self.data["href"] = "/api/robot/body/arms/" + str(uuid) + "/elbow/"

    def get(self, arm_id):
        self.data["href"] = "/api/robot/body/arms/" + str(arm_id) + "/elbow/"
        return marshal(self.data, self.fields)

    def patch(self, arm_id):
        data = request.get_json(force=True)

        self.validate_fields(data)

        for key in data.keys():
            self.data[key] = data[key]

        return marshal(self.data, self.fields), 201


class ElbowSerializer(HingeJointSerializer):
    pass
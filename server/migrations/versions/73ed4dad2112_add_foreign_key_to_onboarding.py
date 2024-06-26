"""add foreign key to onboarding

Revision ID: 73ed4dad2112
Revises: da5e9e0ec1d8
Create Date: 2024-05-02 15:14:10.831604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ed4dad2112'
down_revision = 'da5e9e0ec1d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###

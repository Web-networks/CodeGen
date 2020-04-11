# sed -re 's/^( *)#"([a-z_]*)": "([a-z_]*)".{,2}$/\1\2:\n\1  type: \3/g' models.yaml > models.yaml.new

cat models.yaml \
  | sed -re 's/^( *)type: float/\1type: number\n\1format: float/g' \
  | sed -re 's!type: regularizer!$ref: '\''#/components/schemas/Regularizer'\''!g' \
  | sed -re 's!type: regulizer!$ref: '\''#/components/schemas/Regularizer'\''!g' \
  | sed -re 's!type: activations?!$ref: '\''#/components/schemas/Activation'\''!g' \
  | sed -re 's!type: constraints?!$ref: '\''#/components/schemas/Constraint'\''!g' \
  | sed -re 's!type: initializers?!$ref: '\''#/components/schemas/Initializers'\''!g' \
  > models.yaml.new

diff --color=always -u models.yaml models.yaml.new #| less -FR

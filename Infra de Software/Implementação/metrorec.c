#include <pthread.h>
#include <stdio.h>

struct estacao {

    int passageiros;
    int assentos_livres;

    pthread_mutex_t mutex0;
    
    pthread_cond_t cond_vagao_disponivel;
    pthread_cond_t cond_vagao_cheio;
};

void estacao_init(struct estacao *estacao) {

    estacao->passageiros = 0;
    estacao->assentos_livres = 0;

    pthread_mutex_init(&(estacao->mutex0),NULL);

    pthread_cond_init(&(estacao->cond_vagao_disponivel),NULL);
    pthread_cond_init(&(estacao->cond_vagao_cheio),NULL);
}

void estacao_preencher_vagao(struct estacao * estacao, int assentos) {

    pthread_mutex_lock(&(estacao->mutex0));
    estacao->assentos_livres = assentos;
    pthread_cond_broadcast(&(estacao->cond_vagao_disponivel));
    while (estacao->passageiros == 0 && estacao->assentos_livres == 0) {
        pthread_cond_wait(&(estacao->cond_vagao_cheio),&(estacao->mutex0));
    }
    pthread_mutex_unlock(&(estacao->mutex0));
}

void estacao_espera_pelo_vagao(struct estacao * estacao) {

    pthread_mutex_lock(&(estacao->mutex0));
    estacao->passageiros++;
    while(estacao->assentos_livres == 0){
        pthread_cond_wait(&(estacao->cond_vagao_disponivel), &(estacao->mutex0));
    }
    pthread_mutex_unlock(&(estacao->mutex0));
}

void estacao_embarque(struct estacao * estacao) {

    pthread_mutex_lock(&(estacao->mutex0));
    estacao->passageiros--;
    estacao->assentos_livres--;
    if (estacao->passageiros == 0 || estacao->assentos_livres == 0) {
        pthread_cond_signal(&(estacao->cond_vagao_cheio));
    }
    pthread_mutex_unlock(&(estacao->mutex0));
}